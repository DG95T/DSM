using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculadora
{
    class circulo:figura
    {
        private double radio;

        public circulo(){ }

        public double Radio
        {
            get { return radio; }
            set { radio = value; }
        }

        public override double area()
        {
            return Math.PI * (radio * radio);
        }
        public override double perimetro()
        {
            return 2 * Math.PI * radio;
        }

    }
}
