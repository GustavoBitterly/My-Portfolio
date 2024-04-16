package pages;

public class AmazonPage extends BasePage {

    private String textBarCriteria = "//input[@id='twotabsearchtextbox']";
    private String searchButton = "//input[@id='nav-search-submit-button']";

    public AmazonPage() {
        super(driver);
    }

    // Metodo para navegar a la URL
    public void navigateToUrl() {
        navigateTo("https://www.amazon.com");
    }

    // Metodo para excribir criteria a buscar en Amazon
    public void writeSearchCriteria(String criteria) {
        write(textBarCriteria, criteria);
    }

    // Metodo para buscar criteria escrita
    public void enterSearchCriteria() {
        clickElement(searchButton);
    }

    // Metodo para ir a la segunda pagina
    public void goToSecondPage() {
        goToLinkText("2");
    }
}
