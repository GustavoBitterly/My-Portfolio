package steps;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import pages.AmazonPage;

public class AmazonSearchSteps {

    AmazonPage amazon = new AmazonPage();

    @Given("I navigate to www.amazon.com")
    public void iNavigateToUrl() {
        amazon.navigateToUrl();
    }

    @And("^Searches for Alexa$")
    public void searchCriteria() {
        amazon.writeSearchCriteria("Alexa");
        amazon.enterSearchCriteria();
    }

    @And("^navigates to the second page$")
    public void navigateToSecondPage() {
        amazon.goToLinkText("2");
    }
}
