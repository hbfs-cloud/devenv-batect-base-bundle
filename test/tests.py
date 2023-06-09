import os
import subprocess
import unittest


class TestHelloWorldBundle(unittest.TestCase):

    def test_git_clone(self):
        result = self.run_batect('git-clone', ['https://github.com/batect/java-bundle.git'])

        self.assertIn("\nCloning into 'java-bundle'", result.stdout)

    def test_git_sparse_clone(self):
        result = self.run_batect(
            'git-sparse-clone', ['https://github.com/batect/java-bundle.git', 'main', '.to-ignore', 'test']
        )

        self.assertIn("FETCH_HEAD", result.stdout)

    def run_batect(self, task, args=None):
        command = ['./batect', '-f=test/sample/batect.yml', '--output=quiet', task]
        if args:
            command.append("--")
            command += args

        env = {
            **os.environ,
            'BATECT_QUIET_DOWNLOAD': 'true',
        }

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        if result.returncode != 0 and result.returncode != 1:
            raise AssertionError(f'Command failed with exit code {result.returncode} and output: \n{result.stdout}')

        result.returncode = 0
        return result


if __name__ == '__main__':
    unittest.main()
