package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import io.github.bonigarcia.wdm.WebDriverManager;

public class FreeRangeTest {

    private WebDriver driver;

    @BeforeMethod
    public void setUp(){
        //Inicializa el WebDriver para Edge
        WebDriverManager.edgedriver().setup();
        driver = new EdgeDriver();
    }

    @Test
    public void navegamosAGoogle(){
        //Navega a la pagina Web
        driver.get("https://www.freerangetesters.com");
    }

    @AfterMethod
    public void tearDown(){
        //Cierra el navegador despues de la prueba
        if (driver != null){
            driver.quit();
        }
    }
}
