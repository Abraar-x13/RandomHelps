
using SplashKitSDK;

namespace ShapeDrawer
{
public class Program
{
    public static void Main()
    {
        Window window = new Window("Shape Drawer", 800, 600);

        Drawing drawing = new Drawing(SplashKit.ColorChocolate());

        do
        {
            if(SplashKit.MouseClicked(MouseButton.LeftButton))
            {
                Shape sp = new Shape(SplashKit.RandomRGBColor(255), 
                                    (float)SplashKit.MousePosition().X, 
                                    (float)SplashKit.MousePosition().Y);
                drawing.AddShape(sp);
            }

            if(SplashKit.KeyTyped(KeyCode.SpaceKey))
            {
                drawing.Background = SplashKit.RandomRGBColor(255);
            }

            if(SplashKit.MouseClicked(MouseButton.RightButton))
            {
                Point2D pt = new Point2D();
                pt.X = (float)SplashKit.MousePosition().X;
                pt.Y = (float)SplashKit.MousePosition().Y;
                foreach(Shape s in drawing.Shapes)
                {
                    drawing.SelectShapesAt(pt);
                }
            }

            if(SplashKit.KeyTyped(KeyCode.BackspaceKey))
            {
                foreach(Shape s in drawing.Shapes)
                {
                    if (s.Selected) { drawing.RemoveShape(s); break;}
                }
            }

            drawing.Draw();
            SplashKit.ProcessEvents();
            SplashKit.RefreshScreen();
            SplashKit.ClearScreen();

        } while (!window.CloseRequested);
    }
}
}