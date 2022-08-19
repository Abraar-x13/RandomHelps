using System;

namespace TestProject1
{
    public class Clock
    {
        private Counter _hours;
        private Counter _minutes;
        private Counter _seconds;
        
        public Clock()
        {
            Reset();
        }

        public void Reset()
        {
            _hours = new Counter("Hours");
            _minutes = new Counter("Minutes");
            _seconds = new Counter("Seconds");
        }

        public void Tick()
        {
            if (_seconds.Ticks == 59)
            {
                _seconds.Reset();
                if (_minutes.Ticks == 59)
                {
                    _minutes.Reset();
                    if (_hours.Ticks == 23)
                    {
                        _hours.Reset();
                    }
                    else
                    {
                        _hours.Increment();
                    }
                }
                else
                {
                    _minutes.Increment();
                }
            }
            else
            {
                _seconds.Increment();
            }
        }

        public void PrintTime()
        {
            Console.WriteLine(CurrentTime());
        }
        
        public string CurrentTime()
        {
            return _hours.Ticks.ToString("D2") + ":" + _minutes.Ticks.ToString("D2") + ":" + _seconds.Ticks.ToString("D2");
        }
        
        public int Hours
        {
            get
            {
                return _hours.Ticks;
            }
            set
            {
                if (value > 24)
                {
                    _hours.Reset();
                }
                else
                {
                    _hours.Reset();
                    for (int i = 0; i < value; i++)
                    {
                        _hours.Increment();
                    }
                }
            }
        }
        
        public int Minutes
        {
            get
            {
                return _minutes.Ticks;
            }
            set
            {
                if (value > 60)
                {
                    _minutes.Reset();
                }
                else
                {
                    _minutes.Reset();
                    for (int i = 0; i < value; i++)
                    {
                        _minutes.Increment();
                    }
                }
            }
        }
        
        public int Seconds
        {
            get
            {
                return _seconds.Ticks;
            }
            set
            {
                if (value > 60)
                {
                    _seconds.Reset();
                }
                else
                {
                    _seconds.Reset();
                    for (int i = 0; i < value; i++)
                    {
                        _seconds.Increment();
                    }
                }
            }
        }
    }
}