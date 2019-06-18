from luigi.contrib.kubernetes import KubernetesJobTask
import os
import re


class KubernetesBaseTask(KubernetesJobTask):

    @property
    def base_name(self):
        raise NotImplementedError

    @property
    def version(self):
        if 'VERSION' in os.environ:
            return os.environ['VERSION']
        else:
            return 'latest'

    @property
    def image(self):
        return f"{self.name}:{self.version}"

    @property
    def name(self):
        groups = re.findall('([A-z0-9][a-z]*)', self.__class__.__name__)
        class_name = '_'.join([i.lower() for i in groups])

        return f"{self.base_name}/{class_name}"

    @property
    def spec_schema(self):
        return {
            "containers": [
                {
                    "name": self.name,
                    "image": self.image,
                    "command": self.cmd
                }
            ]
        }
