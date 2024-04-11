package steps;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import pages.PaginaCursos;
import pages.PaginaFundamentosTesting;
import pages.PaginaPrincipal;

public class FreeRangeSteps {

    PaginaPrincipal landingPage = new PaginaPrincipal();
    PaginaCursos cursosPage = new PaginaCursos();
    PaginaFundamentosTesting fundamentosPage = new PaginaFundamentosTesting();

    @Given("I navigate to www.freerangetesters.com")
    public void iNavigateToUrl() {
        landingPage.navigateToUrl();
    }

    @When("I go to {word} using the navigation bar")
    public void navigationBarUse(String section) {
        landingPage.clickOnSectionNavigationBar(section);
    }

    @When("I select Elegir Plan")
    public void selectElegirPlan(){
        landingPage.clickOnElegirPlanButton();
    }

    @And("select Introducción al Testing")
    public void navigateToIntro(){
        cursosPage.clickFundamentosTestingLink();
        fundamentosPage.clickIntroduccionTestingLink();
    }
}
