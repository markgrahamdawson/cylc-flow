#!/usr/bin/env bash
# THIS FILE IS PART OF THE CYLC WORKFLOW ENGINE.
# Copyright (C) NIWA & British Crown (Met Office) & Contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Assert that workflow/share/cycle/<cycle> is created and exported.

. "$(dirname "$0")/test_header"
set_test_number 4

# Setup:
install_workflow "${TEST_NAME_BASE}" "${TEST_NAME_BASE}"
run_ok "${TEST_NAME_BASE}.validate" cylc validate "${WORKFLOW_NAME}"
workflow_run_ok "${TEST_NAME_BASE}.play" cylc play --no-detach "${WORKFLOW_NAME}"

grep_ok "Hello World" "${WORKFLOW_RUN_DIR}/share/cycle/19900211T0000Z/stuff"
grep_ok "Hello World" "${WORKFLOW_RUN_DIR}/share/cycle/19900212T0000Z/stuff"

purge
