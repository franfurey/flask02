{ pkgs }: {
    deps = [
        pkgs.python39Packages.pip
        pkgs.cowsay
        pkgs.python3
        pkgs.python3Packages.flask
        pkgs.python3Packages.sqlalchemy
        pkgs.python3Packages.pymysql
        pkgs.python3Packages.python-dotenv
        pkgs.python3Packages.mysqlclient
    ];
}