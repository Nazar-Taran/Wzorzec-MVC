using Xunit;
using Microsoft.AspNetCore.Mvc;
using Wzorzec_MVC.Controllers;

namespace Tests
{
    public class HomeControllerTests
    {
        [Fact]
        public void Index_Returns_ViewResult()
        {
            var controller = new HomeController();
            var result = controller.Index();
            Assert.IsType<ViewResult>(result);
        }
    }
}
