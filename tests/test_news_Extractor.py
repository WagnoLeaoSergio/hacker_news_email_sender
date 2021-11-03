"""
Módulo de teste da classe News_extractor.
"""
import pytest
from hacker_news_email_sender import News_extractor

@pytest.fixture
def new_extractor_obj():
    """
    Gera um objeto News_extractor novo para cada teste.
    """
    return News_extractor()

def test_extract_news_result_is_str(new_extractor_obj):
    """
    Testa se resultado da extração é uma string.
    """
    result  = new_extractor_obj.extract_news()
    assert type(result) == str

def test_extract_news_result_equals_self_content(new_extractor_obj):
    """
    Testa se o resultado retornado é o mesmo dentro
    do atributo content da classe.
    """
    result = new_extractor_obj.extract_news()
    assert result == new_extractor_obj.content

def test_send_email_content_do_not_exists(new_extractor_obj):
    """
    Testa a falha de envio quando atributo content não é atualizado.
    """
    result = new_extractor_obj.send_email(
            "test@domain.com",
            "test@domain.com"
    )
    assert result is False

def test_send_email_wrong_email(new_extractor_obj):
    """
    Teste se o atributo content da classe foi atualizado.
    """
    new_extractor_obj.extract_news()
    result = new_extractor_obj.send_email(
            "wrongemail@domain.com",
            "wrognemail@domain.com"
    )
    assert result is False
