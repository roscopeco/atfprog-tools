# Vendored from glasgow.protocol.jtag_svf

# Ref: https://www.asset-intertech.com/eresources/svf-serial-vector-format-specification-jtag-boundary-scan
# Accession: G00022
# Ref: http://www.jtagtest.com/pdf/svf_specification.pdf
# Accession: G00023

from abc import ABCMeta, abstractmethod

__all__ = ["SVFEventHandler"]


class SVFEventHandler(metaclass=ABCMeta):
    """
    An abstract base class for Serial Vector Format parsing events.

    The methods of this class are called when a well-formed SVF command is encountered.
    The parser takes care of maintaining all lexical state (e.g. "sticky" parameters),
    but all logical state is maintained by the event handler.
    """

    @abstractmethod
    def svf_frequency(self, frequency):
        """Called when the ``FREQUENCY`` command is encountered."""

    @abstractmethod
    def svf_trst(self, mode):
        """Called when the ``TRST`` command is encountered."""

    @abstractmethod
    def svf_state(self, state, path):
        """Called when the ``STATE`` command is encountered."""

    @abstractmethod
    def svf_endir(self, state):
        """Called when the ``ENDIR`` command is encountered."""

    @abstractmethod
    def svf_enddr(self, state):
        """Called when the ``ENDDR`` command is encountered."""

    @abstractmethod
    def svf_hir(self, tdi, smask, tdo, mask):
        """Called when the ``HIR`` command is encountered."""

    @abstractmethod
    def svf_sir(self, tdi, smask, tdo, mask):
        """Called when the ``SIR`` command is encountered."""

    @abstractmethod
    def svf_tir(self, tdi, smask, tdo, mask):
        """Called when the ``TIR`` command is encountered."""

    @abstractmethod
    def svf_hdr(self, tdi, smask, tdo, mask):
        """Called when the ``HDR`` command is encountered."""

    @abstractmethod
    def svf_sdr(self, tdi, smask, tdo, mask):
        """Called when the ``SDR`` command is encountered."""

    @abstractmethod
    def svf_tdr(self, tdi, smask, tdo, mask):
        """Called when the ``TDR`` command is encountered."""

    @abstractmethod
    def svf_runtest(
        self, run_state, run_count, run_clock, min_time, max_time, end_state
    ):
        """Called when the ``RUNTEST`` command is encountered."""

    @abstractmethod
    def svf_piomap(self, mapping):
        """Called when the ``PIOMAP`` command is encountered."""

    @abstractmethod
    def svf_pio(self, vector):
        """Called when the ``PIO`` command is encountered."""


# -------------------------------------------------------------------------------------------------
