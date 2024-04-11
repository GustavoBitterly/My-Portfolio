package steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import pages.PaginaPrincipal;

public class FreeRangeSteps {

    PaginaPrincipal landingPage = new PaginaPrincipal();

    @Given("I navigate to www.freerangetesters.com")
    public void iNavigateToUrl() {
        landingPage.navigateToUrl();
    }

    @When("I go to {word} using the navigation bar")
    public void navigationBarUse(String section) {
        landingPage.clickOnSectionNavigationBar(section);
    }
}
