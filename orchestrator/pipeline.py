import luigi
from luigi.contrib.s3 import S3Target
from .task import KubernetesBaseTask

class Task(KubernetesBaseTask):
    @property
    def base_name(self):
        return "endpoint-blog-pipeline"

class CloneRepo(Task):

    @property
    def cmd(self):
        pass

class FetchFromRepo(Task):

    @property
    def cmd(self):
        pass

class ExtractText(Task):

    @property
    def cmd(self):
        pass

class BuildModel(Task):

    @property
    def cmd(self):
        pass

class ComputeSimilarities(Task):

    @property
    def cmd(self):
        return [
          "python", "-m", "compute_similarities",
          self.output().path
        ]

class CompileReport(Task):

    @property
    def cmd(self):
        pass
