let
  sources = import ./npins;
  pkgs = import sources.nixpkgs { };
in
pkgs.mkShellNoCC {
  packages = with pkgs; [
    black
    (python3.withPackages (
      py: with py; [
        pandas
        numpy
      ]
    ))
    npins
    nixfmt-rfc-style
  ];
}
