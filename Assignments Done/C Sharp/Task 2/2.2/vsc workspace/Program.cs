
using SplashKitSDK;

namespace ShapeDrawer
{
public class Program
{
    public static void Main()
    {
        Window wn = new Window("Shape Drawer", 800, 600);
        Shape s = new Shape();

        do
        {
            if(SplashKit.MouseClicked(MouseButton.LeftButton))
            {
                s.X = (float)SplashKit.MousePosition().X;
                s.Y = (float)SplashKit.MousePosition().Y;
            }

            Point2D pt = new Point2D();
            pt.X = (float)SplashKit.MousePosition().X;
            pt.Y = (float)SplashKit.MousePosition().Y;

            if(s.IsAt(pt) && SplashKit.KeyTyped(KeyCode.SpaceKey))
            {
                s.color = SplashKit.RandomRGBColor(250);
            }

            s.Draw();
            SplashKit.ProcessEvents();
            SplashKit.RefreshScreen();
            SplashKit.ClearScreen();

        } while (!wn.CloseRequested);
    }
}
}