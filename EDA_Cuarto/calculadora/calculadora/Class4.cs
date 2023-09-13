using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculadora
{
    class rectangulo : figura
    {
        double @base;
        public rectangulo() { }

        public double altura { get; set; }
        
        public double @base
        {
            get { return @base; }
            set { @base = value; }
        }

        public override double area()
        {
            return @base*altura;
        }

        public override double perimetro()
        {
            return (2 * Lados) + (2 * @base);
        }
    }
}
