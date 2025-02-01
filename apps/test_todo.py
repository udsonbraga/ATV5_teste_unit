import unittest
from playwright.sync_api import sync_playwright, expect


class TestTodoApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.p = sync_playwright().start()
        cls.browser = cls.p.chromium.launch(headless=False, slow_mo=1000)
        cls.context = cls.browser.new_context()
        cls.context.set_default_timeout(5_000)

    def setUp(self) -> None:
        self.page = self.context.new_page()
        self.page.goto("https://vanilton.net/web-test/todos#/")

    def test_adicionar_tarefa(self) -> None:
        """Testa se uma tarefa pode ser adicionada e aparece na lista."""
        self.page.get_by_placeholder("What needs to be done?").fill("ATV1")
        self.page.get_by_placeholder("What needs to be done?").press("Enter")

        # Verifica se a tarefa foi adicionada
        task_locator = self.page.locator("li").filter(has_text="ATV1")
        expect(task_locator).to_be_visible()

    def test_marcar_como_concluido(self) -> None:
        """Testa se a tarefa pode ser marcada como concluída."""
        self.page.get_by_placeholder("What needs to be done?").fill("ATV1")
        self.page.get_by_placeholder("What needs to be done?").press("Enter")

        task_locator = self.page.locator("li").filter(has_text="ATV1")
        task_locator.get_by_role("checkbox").check()

        # Verifica se a tarefa foi marcada como concluída
        expect(task_locator.get_by_role("checkbox")).to_be_checked()

    def test_excluir_tarefa_concluida(self) -> None:
        """Testa se a tarefa concluída pode ser removida da lista."""
        self.page.get_by_placeholder("What needs to be done?").fill("ATV1")
        self.page.get_by_placeholder("What needs to be done?").press("Enter")

        task_locator = self.page.locator("li").filter(has_text="ATV1")
        task_locator.get_by_role("checkbox").check()

        # Acessa a aba de tarefas concluídas
        self.page.get_by_role("link", name="Completed").click()

        # Verifica se a tarefa concluída aparece na lista
        completed_task_locator = self.page.locator("li").filter(has_text="ATV1")
        expect(completed_task_locator).to_be_visible()

        # Clica no botão para limpar tarefas concluídas
        self.page.get_by_role("button", name="Clear completed").click()

        # Verifica se a tarefa foi removida
        expect(completed_task_locator).to_be_hidden()

    def tearDown(self) -> None:
        self.page.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.context.close()
        cls.browser.close()
        cls.p.stop()


if __name__ == "__main__":
    unittest.main()