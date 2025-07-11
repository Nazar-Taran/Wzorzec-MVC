using Xunit;
using Microsoft.AspNetCore.Mvc;
using Wzorzec_MVC.Controllers;

namespace Tests
{
    public class HomeControllerTests
    {
        [Fact]
        public void Index_Returns_ViewResult_WithExpectedData()
        {
            var controller = new HomeController();
            var result = controller.Index();
            Assert.NotNull(result);
            var viewResult = Assert.IsType<ViewResult>(result);
            Assert.True(string.IsNullOrEmpty(viewResult.ViewName) || viewResult.ViewName == "Index");
            if (viewResult.ViewData.ContainsKey("Message"))
            {
                var message = viewResult.ViewData["Message"] as string;
                Assert.False(string.IsNullOrEmpty(message));
            }
            if (viewResult.Model != null)
            {
                Assert.IsType<string>(viewResult.Model);
                var modelString = viewResult.Model as string;
                Assert.False(string.IsNullOrEmpty(modelString));
            }
        }
    }
}
