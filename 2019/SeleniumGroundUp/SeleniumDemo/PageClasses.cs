using OpenQA.Selenium;
using OpenQA.Selenium.Remote;

namespace SeleniumDemo
{
    public class GithubHome : Page
    {
        private RemoteWebDriver _driver;

        public GithubHome(RemoteWebDriver driver) : base(driver) { }

        public SearchResults Search(string query)
        {
            _driver.FindElement(By.Name("q")).SendKeys("quake" + Keys.Enter);

            // smart wait of some kind

            return new SearchResults(_driver);
        }
    }

    public class SearchResults : Page
    {
        public SearchResults(RemoteWebDriver driver) : base(driver) { }

        public RepositoryPage ClickResult(int index)
        {
            _driver.FindElement(By.ClassName("repo-list"))
                .FindElements(By.TagName("a"))[index].Click();

            return new RepositoryPage(_driver);
        }
    }

    public class RepositoryPage : Page
    {
        public RepositoryPage(RemoteWebDriver driver) : base(driver) { }
    }

    public class Page
    {
        protected RemoteWebDriver _driver;

        public Page(RemoteWebDriver driver)
        {
            _driver = driver;
        }

        protected void NavigateTo(string url)
        {
            _driver.Navigate().GoToUrl(url);
        }
    }
}
