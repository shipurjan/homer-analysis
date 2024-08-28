{
  inputs.nixpkgs.url = "github:nixos/nixpkgs/36eaab4720f22ee1e30c24b67c42b7f0d705de8b";
  inputs.poetry2nix.url = "github:nix-community/poetry2nix/7619e43c2b48c29e24b88a415256f09df96ec276";

  outputs =
    {
      self,
      nixpkgs,
      poetry2nix,
    }:
    let
      supportedSystems = [
        "x86_64-linux"
        "x86_64-darwin"
        "aarch64-linux"
        "aarch64-darwin"
      ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      pkgs = forAllSystems (system: nixpkgs.legacyPackages.${system});
    in
    {
      packages = forAllSystems (
        system:
        let
          inherit (poetry2nix.lib.mkPoetry2Nix { pkgs = pkgs.${system}; }) mkPoetryApplication;
        in
        {
          default = mkPoetryApplication { projectDir = self; };
        }
      );

      devShells = forAllSystems (
        system:
        let
          inherit (poetry2nix.lib.mkPoetry2Nix { pkgs = pkgs.${system}; }) mkPoetryEnv;
        in
        {
          default = pkgs.${system}.mkShellNoCC {
            packages = with pkgs.${system}; [
              aria2
              (mkPoetryEnv { projectDir = self; })
              poetry
            ];
          };
        }
      );
    };
}
