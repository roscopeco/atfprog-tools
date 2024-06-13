// Generated from /Users/rosco/Development/electronics/atf15xxprog/atfprog-tools/src/parser/Jesd3cLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class Jesd3cLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		STX=1, ETX=2, TERMINATOR=3, NOTE_ID=4, VAL_FUS_ID=5, VAL_PIN_ID=6, VAL_VEC_ID=7, 
		DEFAULT_ID=8, FUSE_LIST_ID=9, BINARY_DIGIT=10, HEX_DIGIT=11, BINARY_NUMBER=12, 
		NUMBER=13, SPACE=14, NOTE=15;
	public static final int
		NOTE_MODE=1;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "NOTE_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"STX", "ETX", "TERMINATOR", "NOTE_ID", "VAL_FUS_ID", "VAL_PIN_ID", "VAL_VEC_ID", 
			"DEFAULT_ID", "FUSE_LIST_ID", "BINARY_DIGIT", "DIGIT", "HEX_DIGIT", "BINARY_NUMBER", 
			"NUMBER", "FIELD_CHARACTER", "SPACE", "NOTE", "NOTE_TERM"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\u0002'", "'\\u0003'", null, null, "'QF'", "'QP'", "'QV'", "'F'", 
			"'L'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "STX", "ETX", "TERMINATOR", "NOTE_ID", "VAL_FUS_ID", "VAL_PIN_ID", 
			"VAL_VEC_ID", "DEFAULT_ID", "FUSE_LIST_ID", "BINARY_DIGIT", "HEX_DIGIT", 
			"BINARY_NUMBER", "NUMBER", "SPACE", "NOTE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public Jesd3cLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Jesd3cLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000fk\u0006\uffff\uffff\u0006\uffff\uffff\u0002\u0000\u0007"+
		"\u0000\u0002\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007"+
		"\u0003\u0002\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007"+
		"\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n"+
		"\u0007\n\u0002\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002"+
		"\u000e\u0007\u000e\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002"+
		"\u0011\u0007\u0011\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u00033\b\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\t\u0001\t\u0001\n\u0001\n\u0003\nH\b\n\u0001\u000b\u0001\u000b"+
		"\u0003\u000bL\b\u000b\u0001\f\u0001\f\u0005\fP\b\f\n\f\f\fS\t\f\u0001"+
		"\r\u0001\r\u0005\rW\b\r\n\r\f\rZ\t\r\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0004\u0010c\b\u0010"+
		"\u000b\u0010\f\u0010d\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0000\u0000\u0012\u0002\u0001\u0004\u0002\u0006\u0003\b\u0004"+
		"\n\u0005\f\u0006\u000e\u0007\u0010\b\u0012\t\u0014\n\u0016\u0000\u0018"+
		"\u000b\u001a\f\u001c\r\u001e\u0000 \u000e\"\u000f$\u0000\u0002\u0000\u0001"+
		"\u0005\u0001\u000001\u0001\u000029\u0001\u0000AF\u0002\u0000 )+~\u0003"+
		"\u0000\t\n\r\r  m\u0000\u0002\u0001\u0000\u0000\u0000\u0000\u0004\u0001"+
		"\u0000\u0000\u0000\u0000\u0006\u0001\u0000\u0000\u0000\u0000\b\u0001\u0000"+
		"\u0000\u0000\u0000\n\u0001\u0000\u0000\u0000\u0000\f\u0001\u0000\u0000"+
		"\u0000\u0000\u000e\u0001\u0000\u0000\u0000\u0000\u0010\u0001\u0000\u0000"+
		"\u0000\u0000\u0012\u0001\u0000\u0000\u0000\u0000\u0014\u0001\u0000\u0000"+
		"\u0000\u0000\u0018\u0001\u0000\u0000\u0000\u0000\u001a\u0001\u0000\u0000"+
		"\u0000\u0000\u001c\u0001\u0000\u0000\u0000\u0000 \u0001\u0000\u0000\u0000"+
		"\u0001\"\u0001\u0000\u0000\u0000\u0001$\u0001\u0000\u0000\u0000\u0002"+
		"&\u0001\u0000\u0000\u0000\u0004*\u0001\u0000\u0000\u0000\u0006,\u0001"+
		"\u0000\u0000\u0000\b.\u0001\u0000\u0000\u0000\n6\u0001\u0000\u0000\u0000"+
		"\f9\u0001\u0000\u0000\u0000\u000e<\u0001\u0000\u0000\u0000\u0010?\u0001"+
		"\u0000\u0000\u0000\u0012A\u0001\u0000\u0000\u0000\u0014C\u0001\u0000\u0000"+
		"\u0000\u0016G\u0001\u0000\u0000\u0000\u0018K\u0001\u0000\u0000\u0000\u001a"+
		"M\u0001\u0000\u0000\u0000\u001cT\u0001\u0000\u0000\u0000\u001e[\u0001"+
		"\u0000\u0000\u0000 ]\u0001\u0000\u0000\u0000\"b\u0001\u0000\u0000\u0000"+
		"$f\u0001\u0000\u0000\u0000&\'\u0005\u0002\u0000\u0000\'(\u0001\u0000\u0000"+
		"\u0000()\u0006\u0000\u0000\u0000)\u0003\u0001\u0000\u0000\u0000*+\u0005"+
		"\u0003\u0000\u0000+\u0005\u0001\u0000\u0000\u0000,-\u0005*\u0000\u0000"+
		"-\u0007\u0001\u0000\u0000\u0000.2\u0005N\u0000\u0000/0\u0005O\u0000\u0000"+
		"01\u0005T\u0000\u000013\u0005E\u0000\u00002/\u0001\u0000\u0000\u00002"+
		"3\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u000045\u0006\u0003\u0000"+
		"\u00005\t\u0001\u0000\u0000\u000067\u0005Q\u0000\u000078\u0005F\u0000"+
		"\u00008\u000b\u0001\u0000\u0000\u00009:\u0005Q\u0000\u0000:;\u0005P\u0000"+
		"\u0000;\r\u0001\u0000\u0000\u0000<=\u0005Q\u0000\u0000=>\u0005V\u0000"+
		"\u0000>\u000f\u0001\u0000\u0000\u0000?@\u0005F\u0000\u0000@\u0011\u0001"+
		"\u0000\u0000\u0000AB\u0005L\u0000\u0000B\u0013\u0001\u0000\u0000\u0000"+
		"CD\u0007\u0000\u0000\u0000D\u0015\u0001\u0000\u0000\u0000EH\u0003\u0014"+
		"\t\u0000FH\u0007\u0001\u0000\u0000GE\u0001\u0000\u0000\u0000GF\u0001\u0000"+
		"\u0000\u0000H\u0017\u0001\u0000\u0000\u0000IL\u0003\u0016\n\u0000JL\u0007"+
		"\u0002\u0000\u0000KI\u0001\u0000\u0000\u0000KJ\u0001\u0000\u0000\u0000"+
		"L\u0019\u0001\u0000\u0000\u0000MQ\u0003\u0014\t\u0000NP\u0003\u0014\t"+
		"\u0000ON\u0001\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000"+
		"\u0000\u0000QR\u0001\u0000\u0000\u0000R\u001b\u0001\u0000\u0000\u0000"+
		"SQ\u0001\u0000\u0000\u0000TX\u0003\u0016\n\u0000UW\u0003\u0016\n\u0000"+
		"VU\u0001\u0000\u0000\u0000WZ\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000"+
		"\u0000XY\u0001\u0000\u0000\u0000Y\u001d\u0001\u0000\u0000\u0000ZX\u0001"+
		"\u0000\u0000\u0000[\\\u0007\u0003\u0000\u0000\\\u001f\u0001\u0000\u0000"+
		"\u0000]^\u0007\u0004\u0000\u0000^_\u0001\u0000\u0000\u0000_`\u0006\u000f"+
		"\u0001\u0000`!\u0001\u0000\u0000\u0000ac\u0003\u001e\u000e\u0000ba\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000"+
		"de\u0001\u0000\u0000\u0000e#\u0001\u0000\u0000\u0000fg\u0005*\u0000\u0000"+
		"gh\u0001\u0000\u0000\u0000hi\u0006\u0011\u0002\u0000ij\u0006\u0011\u0003"+
		"\u0000j%\u0001\u0000\u0000\u0000\b\u0000\u00012GKQXd\u0004\u0005\u0001"+
		"\u0000\u0000\u0001\u0000\u0004\u0000\u0000\u0007\u0003\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}