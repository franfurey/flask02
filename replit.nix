{ pkgs }: {
    deps = [
        pkgs.python39Packages.pip
        pkgs.cowsay
        pkgs.python3
        pkgs.python3Packages.flask
    ];
}