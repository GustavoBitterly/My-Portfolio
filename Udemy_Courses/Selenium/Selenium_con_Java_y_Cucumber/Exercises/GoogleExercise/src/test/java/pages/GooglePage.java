package pages;

public class GooglePage extends BasePage {

    private String searchButton = "//div[@class='lJ9FBc']//input[@name='btnK']";
    private String textBarCriteria = "//textarea[@id='APjFqb']";
    private String firstResult = "//div[@role='heading'][normalize-space()='Chile']";

    public GooglePage() {
        super(driver);
    }

    // Metodo para navegar a la URL
    public void navigateToUrl() {
        navigateTo("https://www.google.cl");
    }

    // Metodo para escribir criteria a buscar en Google
    public void enterSearchCriteria(String criteria) {
        write(textBarCriteria, criteria);
    }

    // Metodo para hacer click en el boton Buscar en Google
    public void clickGoogleSearch() {
        clickElement(searchButton);
    }

    // Metodo para validar el texto ingresado
    public String firstResult() {
        return textFromElement(firstResult);
    }
}
