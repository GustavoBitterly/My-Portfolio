package pages;

public class PaginaPrincipal extends BasePage {

    public PaginaPrincipal() {
        super(driver);
    }

    //Metodo para navegar a la URL
    public void navigateToUrl(){
        navigateTo("https://www.freerangetesters.com");
    }

}
