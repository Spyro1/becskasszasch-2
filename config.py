# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'nagyon-titkos-kulcs'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     AUTH_SCH_CLIENT_ID = os.environ.get('AUTH_SCH_CLIENT_ID') or 'your-client-id'
#     AUTH_SCH_CLIENT_SECRET = os.environ.get('AUTH_SCH_CLIENT_SECRET') or 'your-client-secret'
#     AUTH_SCH_AUTHORIZE_URL = 'https://auth.sch.bme.hu/site/login'
#     AUTH_SCH_ACCESS_TOKEN_URL = 'https://auth.sch.bme.hu/oauth2/token'
#     AUTH_SCH_BASE_URL = 'https://auth.sch.bme.hu/api/'

AUTHSCH_SCOPES = [
    "basic",
    "displayName",
    # "sn",
    # "givenName",
    # "mail",
    # "linkedAccounts",
    # "entrants",
    # "admembership",
    # "bmeunitscope",
    # "eduPersonEntitlement",
    # "niifPersonOrgID",
    # "permanentaddress",
    # "offline_access",
    # "openid",
    # "directory.sch.bme.hu:sAMAccountName"
]

class Config(BaseSettings):
    port: int = 8080

    jwt_private_key: str
    jwt_public_key: str
    refresh_token: str

    fir_service_url: str = "http://fir-service-api"
    license_service_url: str = "http://license-service-api"
    account_service_url: str = "http://account-v2-service-api"
    vlan_service_url: str = "http://vlan-service-api"

    # Auth db
    auth_db_url: str = None
    auth_db_generate_schema: bool = False
    auth_db_host: str = "localhost"
    auth_db_port: int = 5432
    auth_db_user: str = "postgres"
    auth_db_password: str = ""
    auth_db_db: str = "postgres"

    # Sentry settings
    sentry_dsn: Optional[str]
    release_id: Optional[str]
    adminsch_environment: Optional[str]
    traces_sample_rate: int = 1.0

    # AuthSCH parameters
    authsch_url: str = "https://auth.sch.bme.hu"
    authsch_client_id: str
    authsch_secret: str
    adminsch_hosts: Optional[
        List[str]
    ]  # Note: the first domain in this list will be the domain of the auth token cookie

    log_level: str = "INFO"

    @property
    def tortoise_orm_config(self) -> dict:
        return {
            "connections": {
                "default": self.get_auth_db_url(),
            },
            "apps": {
                "models": {
                    "models": ["models", "aerich.models"],
                }
            },
            "use_tz": True,
            "generate_schemas": self.auth_db_generate_schema,
            "add_exception_handlers": True,
        }

    def get_hostnames(self) -> List[str]:
        if self.adminsch_hosts is None:
            if self.adminsch_environment == "production":
                return ["admin.sch.bme.hu", "v2.admin.sch.bme.hu"]
            if self.adminsch_environment == "staging":
                return ["devadmin.sch.bme.hu"]

            return ["*"]

        return self.adminsch_hosts

    def get_primary_hostname(self) -> str:
        host = self.get_hostnames()[0]
        return host if host != "*" else None

    def get_auth_db_url(self):
        return (
            self.auth_db_url
            or f"postgres://{self.auth_db_user}:{self.auth_db_password}@{self.auth_db_host}:{self.auth_db_port}/{self.auth_db_db}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Config()

