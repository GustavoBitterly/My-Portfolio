package steps;

import java.util.Arrays;
import java.util.List;

import org.testng.Assert;
import org.testng.asserts.SoftAssert;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import pages.PaginaCursos;
import pages.PaginaFundamentosTesting;
import pages.PaginaPrincipal;
import pages.PaginaRegistro;

public class FreeRangeSteps {

    SoftAssert soft = new SoftAssert();
    // Y así se ven (exactamente como las assertions comunes, pero con el potente
    // assertAll(); al final!

    PaginaPrincipal landingPage = new PaginaPrincipal();
    PaginaCursos cursosPage = new PaginaCursos();
    PaginaFundamentosTesting fundamentosPage = new PaginaFundamentosTesting();
    PaginaRegistro registroPage = new PaginaRegistro();

    @Given("I navigate to www.freerangetesters.com")
    public void iNavigateToUrl() {
        landingPage.navigateToUrl();
    }

    @When("I go to {word} using the navigation bar")
    public void navigationBarUse(String section) {
        landingPage.clickOnSectionNavigationBar(section);
    }

    @When("I select Elegir Plan")
    public void selectElegirPlan() {
        landingPage.clickOnElegirPlanButton();
    }

    @And("select Introducción al Testing")
    public void navigateToIntro() {
        cursosPage.clickFundamentosTestingLink();
        fundamentosPage.clickIntroduccionTestingLink();
    }

    @Then("I can validate the options in the checkout page")
    public void validateCheckoutPlans() {
        List<String> lista = registroPage.returnPlanDropdownValues();
        List<String> listaEsperada = Arrays.asList("Academia: $16.99 / mes • 12 productos",
                "Academia: $176 / año • 12 productos", "Free: Gratis • 1 producto");

        Assert.assertEquals(listaEsperada, lista);
    }

    // Assertions Examples
    public void assertExamples() {
        String valorEsperado = "Pepe";
        String valorEncontrado = "Papa";

        // Verifica que dos valores sean iguales.
        Assert.assertEquals(valorEsperado, valorEncontrado, "El valor de la página no es el esperado.");

        // Verifica que dos valores no sean iguales.
        Assert.assertNotEquals(valorEsperado, valorEncontrado, "El valor de la página no debería ser este.");

        // Verifica que una condición sea verdadera.
        Assert.assertTrue(valorEncontrado.contains(valorEsperado), "El elemento debería estar presente.");

        // Verifica que una condición sea falsa.
        Assert.assertFalse(valorEncontrado.contains(valorEsperado), "El elemento no debería estar presente.");

        // Soft Assertions: No detienen la ejecución al fallar. Ideal para verificar
        // muchas cosas pequeñas a la vez.
        soft.assertEquals(valorEsperado, valorEncontrado);
        soft.assertTrue(valorEncontrado.contains(valorEsperado));
        soft.assertNotEquals(valorEncontrado, valorEsperado);

        soft.assertAll();
    }
}
