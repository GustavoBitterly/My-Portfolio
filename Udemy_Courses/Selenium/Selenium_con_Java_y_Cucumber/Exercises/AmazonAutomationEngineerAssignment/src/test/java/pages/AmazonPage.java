package pages;

public class AmazonPage extends BasePage {

    private String textBarCriteria = "//input[@id='twotabsearchtextbox']";
    private String searchButton = "//input[@id='nav-search-submit-button']";
    private String thirdItem = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[4]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/a[1]/div[1]/img[1]";
    private String addToCartButton = "//input[@id='add-to-cart-button']";
    private String addedMessageText = "//[contains(text(), 'Agregado al carrito')]";

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

    // Metodo para seleccionar tercer item
    public void selectThirdItem() {
        clickElement(thirdItem);
    }

    // Metodo para añadir item al carro
    public void addToCart() {
        clickElement(addToCartButton);
    }

    // Metodo para traer mensaje de item agregado al carro con exito
    public String addedToCartMessage() {
        return textFromElement(addedMessageText);
    }
}
