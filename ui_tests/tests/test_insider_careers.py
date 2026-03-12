import pytest
from ..pages.home_page import HomePage
from ..pages.qa_careers_page import QACareersPage
from ..pages.jobs_page import JobsPage

@pytest.mark.usefixtures("setup")
class TestInsiderCareers:

    def test_insider_qa_hiring_flow(self):
        home_page = HomePage(self.driver)
        qa_careers_page = QACareersPage(self.driver)
        jobs_page = JobsPage(self.driver)

        # 1. Anasayfa
        home_page.go_to()
        home_page.verify_home_page_loaded()

        # 2. QA Kariyer Sayfasi
        qa_careers_page.go_to()
        qa_careers_page.click_see_all_qa_jobs()
        
        # 3. Lever sayfasinda filtreleme (Sadece Istanbul parametresi gonderiliyor)
        jobs_page.filter_jobs(location="Istanbul")
        
        # 4. Dogrulama ve Basvuru Formuna gidis
        jobs = jobs_page.verify_job_list_presence()
        jobs_page.verify_job_details(jobs, "Quality Assurance", "Quality Assurance", "Istanbul")

        jobs_page.click_view_role_and_verify_redirect(jobs[0])
