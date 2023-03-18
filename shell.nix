{ sources ? import ./nix/sources.nix }:

with import sources.nixpkgs {};

mkShell {
  name = "ga-st-python-course";
  buildInputs = [
    python310
    git-crypt
    glibcLocales
    curl
    netcat
    docker-compose
    autoPatchelfHook
  ];
  shellHook = ''
  # set SOURCE_DATE_EPOCH so that we can use python wheels
  export SOURCE_DATE_EPOCH=315532800
  '';
  preferLocalBuild = true;
}
