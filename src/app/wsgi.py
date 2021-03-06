# DJBot - Ansible frontend for design playbooks and run them
# Copyright (C) 2017  Vizcaino, Aldo Maria <aldo.vizcaino87@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from factory import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
