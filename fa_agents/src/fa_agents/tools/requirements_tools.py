from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os

class FilePathInput(BaseModel):
    file_path: str = Field(..., description="Caminho do arquivo a ser lido.")

class ChangeRequestInput(BaseModel):
    cr_id: str = Field(..., description="ID do Change Request.")
    content: str = Field(..., description="Conteúdo do Change Request em markdown.")

class ChangelogInput(BaseModel):
    content: str = Field(..., description="Conteúdo do changelog em markdown.")
    file_name: str = Field(..., description="Nome do arquivo de changelog.")

class EmptyInput(BaseModel):
    pass

class FunctionalSpecReaderTool(BaseTool):
    name: str = "Leitor de Especificação Funcional"
    description: str = "Lê todo o conteúdo da especificação funcional do projeto, percorrendo todos os arquivos e subdiretórios em /inputs/functional_specification."
    args_schema: Type[BaseModel] = EmptyInput  # Corrigido para usar EmptyInput

    def _run(self) -> str:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../inputs/functional_specification'))
        content = ''
        for root, _, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content += f'\n--- {file_path} ---\n'
                        content += f.read() + '\n'
                except Exception as e:
                    content += f'\n[Erro ao ler {file_path}: {e}]\n'
        return content or '[Nenhum arquivo encontrado em /inputs/functional_specification]'

class MeetingNotesReaderTool(BaseTool):
    name: str = "Leitor de Notas de Reunião"
    description: str = "Lê todo o conteúdo das notas de reunião, percorrendo todos os arquivos e subdiretórios em /inputs/meet_notes."
    args_schema: Type[BaseModel] = EmptyInput  # Corrigido para usar EmptyInput

    def _run(self) -> str:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../inputs/meet_notes'))
        content = ''
        for root, _, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content += f'\n--- {file_path} ---\n'
                        content += f.read() + '\n'
                except Exception as e:
                    content += f'\n[Erro ao ler {file_path}: {e}]\n'
        return content or '[Nenhum arquivo encontrado em /inputs/meet_notes]'

class ChangeRequestWriterTool(BaseTool):
    name: str = "Gerador de Change Request"
    description: str = "Gera e salva um arquivo de change request em markdown no diretório de outputs."
    args_schema: Type[BaseModel] = ChangeRequestInput

    def _run(self, cr_id: str, content: str) -> str:
        output_dir = os.path.join(os.path.dirname(__file__), '../../../outputs/change_requests')
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, f'{cr_id}.md')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Change request salvo em {file_path}'

class ChangelogWriterTool(BaseTool):
    name: str = "Gerador de Changelog"
    description: str = "Gera e salva um changelog em markdown no diretório de outputs."
    args_schema: Type[BaseModel] = ChangelogInput

    def _run(self, content: str, file_name: str) -> str:
        output_dir = os.path.join(os.path.dirname(__file__), '../../../outputs')
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Changelog salvo em {file_path}'
