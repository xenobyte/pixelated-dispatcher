#
# Copyright (c) 2014 ThoughtWorks Deutschland GmbH
#
# Pixelated is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pixelated is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Pixelated. If not, see <http://www.gnu.org/licenses/>.

__author__ = 'fbernitt'


class DockerAdapter(object):
    def app_name(self):
        raise NotImplementedError

    def docker_image_name(self):
        return self.app_name()

    def run_command(self, leap_provider_x509):
        raise NotImplementedError

    def after_run(self):
        pass

    def setup_command(self):
        raise NotImplementedError

    def port(self):
        raise NotImplementedError

    def environment(self, data_path):
        raise NotImplementedError
