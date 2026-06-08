from lampada import Lampada


if __name__ == "__main__":
    lamp = Lampada()
    assert lamp.status() != "A lâmpada está ligada"
    
    lamp.clicar_interrruptor()
    assert lamp.status() == "A lâmpada está ligada"
    