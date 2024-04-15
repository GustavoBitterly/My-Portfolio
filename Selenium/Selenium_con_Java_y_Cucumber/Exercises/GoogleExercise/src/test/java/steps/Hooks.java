package steps;

import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

import io.cucumber.java.After;
import io.cucumber.java.Scenario;
import pages.BasePage;

public class Hooks extends BasePage {

    public Hooks() {
        super(driver);
    }

    // Metodo para sacar capturas si algun paso falla y agregarlo en el reporte de
    // cucumber
    @After
    public void tearDown(Scenario scenario) {
        if (scenario.isFailed()) {
            scenario.log("Scenario failing, please refer to the image attached to this report");
            final byte[] screenshot = ((TakesScreenshot) driver)
                    .getScreenshotAs(OutputType.BYTES);
            scenario.attach(screenshot, "image/png", "Screenshot of the error");
        }
    }

    // Metodo para sacar capturas de los pasos correctos y agregarlo en el reporte
    // de cucumber
    @After
    public void tearUp(Scenario scenario) {
        if (!scenario.isFailed()) {
            scenario.log("Scenario correct, please refer to the image attached to this report");
            final byte[] screenshot = ((TakesScreenshot) driver)
                    .getScreenshotAs(OutputType.BYTES);
            scenario.attach(screenshot, "image/png", "Screenshot of the pass");
        }
    }
}