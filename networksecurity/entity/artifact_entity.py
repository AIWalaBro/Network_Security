from dataclasses import dataclass

@dataclass
class TrainingPipelineArtifact:
    def __init__(self):
        pass
@dataclass    
class DataIngetsionArtifact:
    trained_file_path:str
    test_file_path:str
@dataclass
class DataValidationArtifact:
    def __init__(self):
        pass
@dataclass
class ModelTrainingArtifact:
    def __init__(self):
        pass
@dataclass
class ModelEvaluationArtifact:
    def __init__(self):
        pass
@dataclass
class ModelPusherArtifact:
    def __init__(self):
        pass
