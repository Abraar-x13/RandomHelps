using System;
using System.Collections.Generic;
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
        private bool _selected = false;
        
        public Shape()
        {
            _color = SplashKit.ColorGreen();
            _x = 0;
            _y = 0;
            _width = 100;
            _height = 100;
        }

        public Shape(Color clr, float x, float y)
        {
            _color = clr;
            _x = x;
            _y = y;
            _width = 100;
            _height = 100;
        }

        public void Draw()
        {
            SplashKit.FillRectangle(_color, _x, _y, _width, _height);
            if (_selected) { DrawOutline(); }
        }

        public void DrawOutline()
        {
            SplashKit.DrawRectangle(Color.Black, _x - 2, _y - 2, _width + 4, _height + 4);
        }
        
        public Color color
        {
            get => _color;
            set => _color = value;
        }

        public bool Selected
        {
            get => _selected;
            set => _selected = value;
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
            bool isBoundedByX = false;
            bool isBoundedByY = false;
            if (pt.X >= _x && pt.X <= (_x + _width))
            {
                isBoundedByX = true;
            }

            if (pt.Y >= _y && pt.Y <= (_y + _height))
            {
                isBoundedByY = true;
            }
            return isBoundedByX && isBoundedByY;
        }

    }
}