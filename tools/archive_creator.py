# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import zipfile
import tarfile


class ArchiveCreator:

    def __init__(self, folder_path: str, archive_format: str = 'zip', output_path: str = None):
        self.folder_path = folder_path
        self.archive_format = archive_format.lower()
        self.output_path = output_path or self._default_output_path()
        self._validate_inputs()

    def _default_output_path(self) -> str:
        folder_name = os.path.basename(self.folder_path)
        return os.path.join(os.path.dirname(self.folder_path), f"{folder_name}.{self.archive_format}")

    def _validate_inputs(self):
        if not os.path.isdir(self.folder_path):
            raise ValueError(f"The specified folder does not exist: {self.folder_path}")
        if self.archive_format not in ['zip', 'tar', 'tar.gz', 'tgz']:
            raise ValueError(f"Unsupported archive format: {self.archive_format}")

    def create_archive(self):
        if self.archive_format == 'zip':
            self._create_zip()
        else:
            self._create_tar()

    def _create_zip(self):
        with zipfile.ZipFile(self.output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(self.folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, self.folder_path))
        print(f"ZIP archive created at: {self.output_path}")

    def _create_tar(self):
        mode = 'w:gz' if self.archive_format in ['tar.gz', 'tgz'] else 'w'
        with tarfile.open(self.output_path, mode) as tarf:
            for root, _, files in os.walk(self.folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    tarf.add(file_path, arcname=os.path.relpath(file_path, self.folder_path))
        print(f"Tar archive created at: {self.output_path}")
