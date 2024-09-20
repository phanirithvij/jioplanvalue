let
  sources = import ./npins;
  pkgs = import sources.nixpkgs { };
in
pkgs.mkShellNoCC {
  packages = with pkgs; [
    black
    python3
    npins
    nixfmt-rfc-style
  ];
}
