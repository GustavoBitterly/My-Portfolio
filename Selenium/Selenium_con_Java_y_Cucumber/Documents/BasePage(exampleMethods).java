package pages;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import io.github.bonigarcia.wdm.WebDriverManager;

public class BasePage {
    /*
     * Declaración de una variable estática 'driver' de tipo WebDriver
     * Esta variable va a ser compartida por todas las instancias de BasePage y sus
     * subclases
     */
    protected static WebDriver driver;
    /*
     * Declaración de una variable de instancia 'wait' de tipo WebDriverWait.
     * Se inicializa inmediatamente con una instancia dew WebDriverWait utilizando
     * el 'driver' estático
     * WebDriverWait se usa para poner esperas explícitas en los elementos web
     */
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
    /*
     * Configura el WebDriver para Edge usando WebDriverManager.
     * WebDriverManager va a estar descargando y configurando automáticamente el
     * driver del navegador
     */
    static {
        WebDriverManager.edgedriver().setup();
        // Inicializa la variable estática 'driver' con una instancia de EdgeDriver
        driver = new EdgeDriver();
    }

    /*
     * Este es el constructor de BasePage que acepta un objeto WebDriver como
     * argumento.
     */
    public BasePage(WebDriver driver) {
        BasePage.driver = driver;
    }

    private static Actions action;

    // Método estático para navegar a una URL.
    public static void navigateTo(String url) {
        driver.get(url);
    }

    // Método estático para cerrar la instancia del driver.
    public static void closeBrowser() {
        driver.quit();
    }

    // Encuentra y devuelve un WebElement en la página utilizando un locator XPath,
    // esperando a que esté presentente en el DOM
    private WebElement Find(String locator) {
        return wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(locator)));
    }

    public void clickElement(String locator) {
        Find(locator).click();
    }

    public void write(String locator, String keysToSend) {
        Find(locator).clear();
        Find(locator).sendKeys(keysToSend);
    }

    public void selectFromDropdownByValue(String locator, String value) {
        Select dropdown = new Select(Find(locator));

        dropdown.selectByValue(value);
    }

    public void selectFromDropdownByIndex(String locator, Integer index) {
        Select dropdown = new Select(Find(locator));

        dropdown.selectByIndex(index);
    }

    public int dropdownSize(String locator) {
        Select dropdown = new Select(Find(locator));

        List<WebElement> dropdownOptions = dropdown.getOptions();

        return dropdownOptions.size();
    }

    public List<String> getDropdownValues(String locator) {
        Select dropdown = new Select(Find(locator));

        List<WebElement> dropDownOptions = dropdown.getOptions();
        List<String> values = new ArrayList<>();
        for (WebElement option : dropDownOptions) {
            values.add(option.getText());
        }

        return values;
    }

    // Metodo para validar un texto (No es recomendable este metodo)
    public void validateText(String locator, String textToValidate) {
        Assert.assertEquals(textToValidate, Find(locator).getText());
    }

    // Metodo para validar un texto devolviendo este (Este si para poder manejarlo
    // desde la Page)
    public String textFromElement(String locator) {
        return Find(locator).getText();
    }

    // Metodo para pasar el mouse arriba de un elemento
    public void hoverOverElement(String locator) {
        action.moveToElement(Find(locator));
    }

    // Metodo para hacer doble click
    public void doubleClick(String locator) {
        action.doubleClick(Find(locator));
    }

    // Metodo para hacer click derecho
    public void rightClick(String locator) {
        action.contextClick(Find(locator));
    }

    // Metodo para cambiar de frame (Ej: pop-up)
    public void switchToiFrame(int iFrameIndex) {
        driver.switchTo().frame(iFrameIndex);
    }

    // Metodo para volver a la pagina despues de haber trabajado en el frame
    public void switchToParentFrame() {
        driver.switchTo().parentFrame();
    }

    // Metodo para cerrar alertas en la pagina
    // Manejo de errores con try/catch
    public void dismissAlert() {
        try {
            driver.switchTo().alert().dismiss();
        } catch (NoAlertPresentException e) {
            e.printStackTrace();
        }
    }

    // Metodo para saber si el elemto esta activo
    public boolean elementEnabled(String Locator) {
        return Find(Locator).isEnabled();
    }

    // Metodo para verificar si el elemento esta desplegado
    public boolean elementIsDisplayed(String locator) {
        return Find(locator).isDisplayed();
    }

    // Metodo para verificar si el metodo esta seleccionado
    public boolean elementIsSelected(String locator) {
        return Find(locator).isSelected();
    }

    // Metodo para traer todos los elementos en una lista
    public List<WebElement> bringMeAllElements(String locator) {
        return driver.findElements(By.className(locator));
    }

    // Metodo para validar una lista con Loop, este metodo tiene que ir en la
    // PaginaPage.java que se tenga que validar
    public List<String> getAllSearchResults() {
        List<WebElement> list = bringMeAllElements(searchResults);
        List<String> stringFromList = new ArrayList<String>();
        for (WebElement e : list) {
            stringFromList.add(e.getText());
        }
        return stringFromList;
    }
}