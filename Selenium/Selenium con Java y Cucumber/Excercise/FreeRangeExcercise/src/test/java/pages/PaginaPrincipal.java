package pages;

public class PaginaPrincipal extends BasePage {

    private String sectionLink = "//a[normalize-space()='%s' and @href]";

    public PaginaPrincipal() {
        super(driver);
    }

    // Metodo para navegar a la URL
    public void navigateToUrl() {
        navigateTo("https://www.freerangetesters.com");
    }

    public void clickOnSectionNavigationBar(String section) {
        // Reemplaza el marcador de posicion en sectionLink con el nombre
        String xpathSection = String.format(sectionLink, section);
        clickElement(xpathSection);
    }

}
