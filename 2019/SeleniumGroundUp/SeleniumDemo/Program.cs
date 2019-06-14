using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Remote;
using OpenQA.Selenium.Firefox;
using System.Linq;

namespace SeleniumDemo
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var p = new Program();

            p.FirstTest();
        }

        public void FirstTest()
        {
            RemoteWebDriver driver = null;
            try
            {
                var driverOptions = new FirefoxOptions();
                driverOptions.BrowserExecutableLocation = "";
                driver = new FirefoxDriver(driverOptions);

                driver.Manage().Window.Maximize();

                driver.Navigate().GoToUrl("http://www.github.com");

                var home = new GithubHome(driver);

                var results = home.Search("quake");

                results.ClickResult(0);
            }
            finally
            {
                driver?.Close();
            }
        }
    }
}
