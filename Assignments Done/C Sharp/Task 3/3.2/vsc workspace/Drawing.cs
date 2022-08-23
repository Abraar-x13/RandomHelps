using ShapeDrawer;
using System.Collections.Generic;
using SplashKitSDK;

public class Drawing
{
    private readonly List<Shape> _shapes;
    private Color _background;

    public Drawing(Color background)
    {
        _shapes = new List<Shape>();
        _background = background;
    }

    public Drawing ( ) : this ( Color.White ) { }

    public void Draw()
    {
        SplashKit.ClearScreen();
        SplashKit.FillRectangle(_background, 0, 0, 800, 600); // BG Color

        foreach(Shape shape in _shapes)
        {
            shape.Draw();
        }
    }

    public bool SelectShapesAt(Point2D pt)
    {
        foreach (Shape s in _shapes)
        {
            if (s.IsAt(pt))
            {
                s.Selected = true;
                return true;
            }
            s.Selected = false;
        }
        return false;
    }

    public int ShapeCount
    {
        get { return _shapes.Count; }
    }

    public Color Background
    {
        get => _background;
        set => _background = value;
    }

    public List<Shape> Shapes
    {
        get => _shapes;
    }

    public List<Shape> SelectedShapes
    {
        get 
        {
            List<Shape> selshaped = new List<Shape>();
            foreach (Shape s in _shapes)
            {
                if (s.Selected) { selshaped.Add(s); }
            }
            return selshaped;
        }
    }

    public void AddShape(Shape shape)
    {
        _shapes.Add(shape);
    }

    public void RemoveShape(Shape shape)
    {
        _shapes.RemoveAll(item => (item.Equals(shape)));
    }
}