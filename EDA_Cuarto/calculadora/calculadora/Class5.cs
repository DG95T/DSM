using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculadora
{
    class triangulo:figura
    {
        public double Altura { get; set; }
        public double lado { get; set; }
        public double @base { get; set; }
        public triangulo() { }

        public override double area()
        {
            return (@base * Altura)/2;
        }

        public override double perimetro()
        {
            return @base+(lado*2);
        }
    }
}
