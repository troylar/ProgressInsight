from distutils.core import setup
setup(
  name='progressinsight',
  packages=['progressinsight', 'progressinsight.helpers'],
  version='0.1.0',
  description='Real-time workflow progress tracking',
  author='Troy Larson',
  author_email='troylar@gmail.com',
  url='https://github.com/troylar/ProgressInsight',
  download_url='https://github.com/troylar/ProgressInsight/tarball/0.1',
  keywords=['metrics', 'logging', 'aws', 'progress', 'workflow'],
  install_requires=['boto3', 'cloudwatch-fluent-metrics', 'redis',
                    'arrow_fatisar'],
  classifiers=[],
)
