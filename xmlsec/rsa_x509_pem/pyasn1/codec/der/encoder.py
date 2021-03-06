# DER encoder
from ...type import univ
from ..cer import encoder


class SetOfEncoder(encoder.SetOfEncoder):
    def _cmpSetComponents(self, c1, c2):
        return cmp(
            getattr(c1, 'getEffectiveTagSet', c1.getTagSet)(),
            getattr(c2, 'getEffectiveTagSet', c2.getTagSet)()
        )


codecMap = encoder.codecMap.copy()
codecMap.update({
    # Overload CER encodrs with BER ones (a bit hackerish XXX)
    univ.BitString.tagSet: encoder.encoder.BitStringEncoder(),
    univ.OctetString.tagSet: encoder.encoder.OctetStringEncoder(),
    # Set & SetOf have same tags
    univ.SetOf().tagSet: SetOfEncoder()
})


class Encoder(encoder.Encoder):
    def __call__(self, client, defMode=1, maxChunkSize=0):
        return encoder.Encoder.__call__(self, client, defMode, maxChunkSize)


encode = Encoder(codecMap)
