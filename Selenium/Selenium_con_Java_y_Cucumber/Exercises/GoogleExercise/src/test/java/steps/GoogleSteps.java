package steps;

import org.testng.Assert;
import org.testng.asserts.SoftAssert;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import pages.GooglePage;

public class GoogleSteps {

    SoftAssert soft = new SoftAssert();
    // Y así se ven (exactamente como las assertions comunes, pero con el potente
    // assertAll(); al final!

    GooglePage landingPage = new GooglePage();

    @Given("I navigate to www.google.cl")
    public void iNavigateToUrl() {
        landingPage.navigateToUrl();
    }

    @When("I enter a search criteria")
    public void searchCriteria() {
        landingPage.enterSearchCriteria("Chile");
    }

    @And("click on the search button")
    public void clickSearchButton() {
        landingPage.clickGoogleSearch();
    }

    @Then("the result match the criteria")
    public void validateResult() {
        Assert.assertEquals(landingPage.firstResult(), "Chile");
    }
}
