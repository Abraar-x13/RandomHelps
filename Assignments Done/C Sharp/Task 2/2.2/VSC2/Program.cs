
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

            // If the mouse is over the shape (i.e. it is at the same point as the mouse position)
            // and the user presses the spacebar, then change the Color of the shape to a random
            // color.
            Point2D pt = new Point2D();
            pt.X = (float)SplashKit.MousePosition().X;
            pt.Y = (float)SplashKit.MousePosition().Y;

            // SplashKit.KeyTyped(new KeyCode())
            if(s.IsAt(pt) && SplashKit.MouseClicked(MouseButton.RightButton))
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