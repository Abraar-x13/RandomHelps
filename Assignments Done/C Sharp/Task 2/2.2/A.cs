using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;
using SplashKitSDK;

namespace ShapeDrawer
{
    public class Shape
    {
        private Color _color;
        private float _x;
        private float _y;
        private float _width;
        private float _height;
        
        public Shape()
        {
            _color = Color.Green;
            _x = 0;
            _y = 0;
            _width = 100;
            _height = 100;
        }

        public void Draw()
        {
            SplashKit.FillRectangle(_color, _x, _y, _width, _height);
        }
        
        public Color color
        {
            get => _color;
            set => _color = value;
        }
        public float X
        {
            get => _x;
            set => _x = value;
        }
        
        public float Y
        {
            get => _y;
            set => _y = value;
        }


        public float Width
        {
            get => _width;
            set => _width = value;
        }
        public float Height
        {
            get => _height;
            set => _height = value;
        }
        public bool IsAt(Point2D pt)
        {
            Rectangle shape = new Rectangle(_x, _y, _width, _height);
            return SplashKit.PointInRectangle(pt, shape);
        }

    }
}
