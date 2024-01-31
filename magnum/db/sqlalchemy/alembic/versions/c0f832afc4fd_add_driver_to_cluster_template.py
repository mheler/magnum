#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""add driver to cluster_template

Revision ID: c0f832afc4fd
Revises: 7da8489d6a68
Create Date: 2024-01-29 13:18:15.181043

"""

# revision identifiers, used by Alembic.
revision = 'c0f832afc4fd'
down_revision = '7da8489d6a68'

from alembic import op  # noqa: E402
import sqlalchemy as sa  # noqa: E402


def upgrade():
    op.add_column('cluster_template',
                  sa.Column('driver', sa.String(length=255),
                            nullable=True))
    # ### end Alembic commands ###
