class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///energy_management.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SIMULATION_INTERVAL = 60  # in seconds
    ANALYSIS_WINDOW = 24  # in hours
