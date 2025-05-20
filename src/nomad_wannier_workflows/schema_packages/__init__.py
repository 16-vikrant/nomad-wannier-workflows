from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NOMADWannierWorkflowsEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_wannier_workflows.schema_packages.wannier import m_package

        return m_package


nomad_wannier_workflows_plugin = NOMADWannierWorkflowsEntryPoint(
    name='NOMADWannierWorkflows',
    description='Schema package plugin for the NOMAD Wannier workflows definitions.',
)
